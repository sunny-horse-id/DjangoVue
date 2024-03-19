<script setup>

</script>

<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light" style="width: 100%">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <div class="dropdown-menu">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <div style="width: 700px"></div>
        <form>
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        </form>
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </div>
    </nav>
    
    <div style="height: 10px; background-color: rgba(222,218,194,0.47)"></div>
    <div class="container-fluid text-center"
         style="background-color: #313133; padding-top: 10px;">
      <div class="copyright">
        <p>
          <a href="javascript:;">关于我们</a>
          <a href="javascript:;">帮助中心</a>
          <a href="javascript:;">搜索推荐</a>
          <a href="javascript:;">友情链接</a>
        </p>
        <p>CopyRight © 舞</p>
      </div>
    </div>
</template>

<style scoped>
.copyright {
  height: 120px;
  padding-top: 40px;
  text-align: center;
  color: #999;
  font-size: 15px;

  p {
    line-height: 1;
    margin-bottom: 20px;
  }

  a {
    color: #999;
    line-height: 1;
    padding: 0 10px;
    border-right: 1px solid #999;

    &:last-child {
      border-right: none;
    }
  }
}
</style>