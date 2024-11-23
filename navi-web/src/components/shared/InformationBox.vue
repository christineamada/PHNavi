<template>
  <Card class="w-[300px]">
    <template #title>
      <div class="flex flex-row justify-between align-middle">
        Welcome to NaVi!<Chip
        /></div
    ></template>
    <template #content>
      <div class="flex flex-col justify-center items-center">
        <header>
          <img
            alt="Logo"
            src="@/assets/images/logo.png"
            class="w-[125px] h-[125px]"
          />
        </header>
        <Divider />
        <p>
          The platform seeks to enhance travel efficiency, reduce congestion,
          and promote sustainable practices.
        </p>
      </div>
    </template>
  </Card>
</template>
