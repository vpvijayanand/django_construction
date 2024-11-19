
    // const csrfToken = "{{ csrf_token }}";

    // // Add event listener to hide warning when user starts typing
    // document.getElementById('new-name').addEventListener('input', function() {
    //     document.getElementById('empty-warning').style.display = 'none';
    // });

    // // Create Employee Type
    // document.getElementById('create-btn').addEventListener('click', function () {
    //     const name = document.getElementById('new-name').value.trim();
    //     if (name === '') {
    //         document.getElementById('empty-warning').style.display = 'block';
    //         return;
    //     }
    //     fetch("/masters/employee-types/create/", {
    //         method: "POST",
    //         headers: { "X-CSRFToken": csrfToken, "Content-Type": "application/x-www-form-urlencoded" },
    //         body: `name=${name}`
    //     })
    //     .then(response => response.json())
    //     .then(data => location.reload());
    // });

    // // Edit Employee Type
    // document.querySelectorAll('.edit-btn').forEach(btn => {
    //     btn.addEventListener('click', function () {
    //         const row = this.closest('tr');
    //         row.querySelector('.view-mode').style.display = 'none';
    //         row.querySelector('.edit-mode').style.display = 'block';
    //         row.querySelector('.save-btn').style.display = 'inline-block';
    //         this.style.display = 'none';
    //     });
    // });

    // // Save Employee Type
    // document.querySelectorAll('.save-btn').forEach(btn => {
    //     btn.addEventListener('click', function () {
    //         const row = this.closest('tr');
    //         const id = row.id.split('-')[1];
    //         const name = row.querySelector('.edit-mode').value;

    //         fetch(`/masters/employee-types/update/${id}/`, {
    //             method: "POST",
    //             headers: { "X-CSRFToken": csrfToken, "Content-Type": "application/x-www-form-urlencoded" },
    //             body: `name=${name}`
    //         })
    //         .then(response => response.json())
    //         .then(data => location.reload());
    //     });
    // });

    // // Delete Employee Type
    // document.querySelectorAll('.delete-btn').forEach(btn => {
    //     btn.addEventListener('click', function () {
    //         if (confirm("Are you sure you want to delete this?")) {
    //             const row = this.closest('tr');
    //             const id = row.id.split('-')[1];

    //             fetch(`/masters/employee-types/delete/${id}/`, {
    //                 method: "POST",
    //                 headers: { "X-CSRFToken": csrfToken }
    //             })
    //             .then(response => response.json())
    //             .then(data => location.reload());
    //         }
    //     });
    // });

    // // Toggle dropdown
    // function toggleDropdown() {
    //     document.getElementById("brandTypeDropdown").classList.toggle("show");
    // }

    // // Close the dropdown if the user clicks outside of it
    // window.onclick = function(event) {
    //     if (!event.target.matches('.custom-dropdown-toggle')) {
    //         var dropdowns = document.getElementsByClassName("dropdown-menu");
    //         for (var i = 0; i < dropdowns.length; i++) {
    //             var openDropdown = dropdowns[i];
    //             if (openDropdown.classList.contains('show')) {
    //                 openDropdown.classList.remove('show');
    //             }
    //         }
    //     }
    // }
    document.addEventListener('DOMContentLoaded', function() {
        const dropdown = document.querySelector('.dropdown');
        const dropdownTrigger = dropdown.querySelector('.nav-item');

        dropdownTrigger.addEventListener('click', function(e) {
            e.preventDefault();
            dropdown.classList.toggle('active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('active');
            }
        });

        // Keyboard accessibility
        dropdownTrigger.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    });
