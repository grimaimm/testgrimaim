def skills_svg():
    html = """
            <div>
              <div class="relative inline-block">
                <div class="tooltip-container relative">
                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" class="text-orange-500" height="24" width="24" xmlns="http://www.w3.org/2000/svg">
                    <title></title>
                    <path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.564-2.438L1.5 0zm7.031 9.75l-.232-2.718 10.059.003.23-2.622L5.412 4.41l.698 8.01h9.126l-.326 3.426-2.91.804-2.955-.81-.188-2.11H6.248l.33 4.171L12 19.351l5.379-1.443.744-8.157H8.531z"></path>
                  </svg>
                  <div class="tooltip-content hidden lg:block bottom-full mb-2 bg-neutral-700 dark:bg-neutral-200 text-neutral-200 dark:text-neutral-700 text-xs rounded px-2 py-1 absolute w-max max-w-xs">HTML</div>
                </div>
              </div>
            </div>
          """

    tailwindCSS = """
            <div>
              <div class="relative inline-block">
                <div class="tooltip-container relative">
                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" class="text-cyan-300" height="24" width="24" xmlns="http://www.w3.org/2000/svg">
                    <title></title>
                    <path d="M12.001,4.8c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 C13.666,10.618,15.027,12,18.001,12c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C16.337,6.182,14.976,4.8,12.001,4.8z M6.001,12c-3.2,0-5.2,1.6-6,4.8c1.2-1.6,2.6-2.2,4.2-1.8c0.913,0.228,1.565,0.89,2.288,1.624 c1.177,1.194,2.538,2.576,5.512,2.576c3.2,0,5.2-1.6,6-4.8c-1.2,1.6-2.6,2.2-4.2,1.8c-0.913-0.228-1.565-0.89-2.288-1.624 C10.337,13.382,8.976,12,6.001,12z"></path>
                  </svg>
                  <div class="tooltip-content hidden lg:block bottom-full mb-2 bg-neutral-700 dark:bg-neutral-200 text-neutral-200 dark:text-neutral-700 text-xs rounded px-2 py-1 absolute w-max max-w-xs">TailwindCSS</div>
                </div>
              </div>
            </div>
          """

    return html, tailwindCSS
