


```markdown
# 🚀 Shovel 快速部署指南

## 环境准备
✅ **最低配置要求**  
- 操作系统：Ubuntu 20.04+/CentOS 7+  
- 内存：2GB+  
- 磁盘：4GB+ 可用空间  
- 网络：开放80/443端口  

​```bash
# 验证磁盘空间（必须≥4GB）
[ $(df -BG / | awk 'NR==2{print $4+0}') -ge 4 ] || { echo "错误：磁盘空间不足，至少需要4GB可用空间"; exit 1; }

# 检查端口开放状态
sudo lsof -i :80
```

---

## 一键部署流程



```bash
#####
```

🔄 **安装过程将自动完成以下操作**：  

1. 初始化Docker环境  
2. 下载基础镜像（约1GB）   
3. 部署核心服务组件  
4. 加载插件（速度根据服务器性能而定）

---

## 📲 验证码获取流程

当出现以下提示时：  

```
请输入镜像激活码：
```

1. 访问公众号 中龙技术
2. 发送关键词 **SHOVEL-ACTIVATE**  
3. 获取验证码

---

## ⚙️ 自定义配置（可选）

### 设置管理员密码

![image-20250216180726824](C:\Users\kdx10\AppData\Roaming\Typora\typora-user-images\image-20250216180726824.png)

---

## 🎉 部署完成验证

1. 访问控制台  
   `http://<你的服务器IP>`

2. 登录验证  

   ```
   默认账号：admin
   初始密码：安装过程中设置的密码
   ```

3. 查看服务状态  

```bash
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
```

---

## 🚨 常见问题排查

### 端口冲突处理

```bash
# 查看占用80端口的进程
sudo lsof -i :80

# 临时释放端口
sudo systemctl stop xxx
```



Shovel 创新地引入了资产组和策略，让工作更加高效便捷，所以让我们从新建资产组开始

1. **创建资产组和负责实体：** 将相关资产分组，并指定负责实体以便管理。

   ![image-20250216200516770](C:\Users\kdx10\AppData\Roaming\Typora\typora-user-images\image-20250216200516770.png)

   

2. **创建策略：** 选择目标资产组，并根据场景配置不同插件，可以批量导入，直接粘贴进多行ip或域名即可。

   

   ![image-20250216201011438](C:\Users\kdx10\AppData\Roaming\Typora\typora-user-images\image-20250216201011438.png)

   

3. **开始任务：** 选择策略即可开始任务，也可手动导入和管理资产。

   ![image-20250216201053020](C:\Users\kdx10\AppData\Roaming\Typora\typora-user-images\image-20250216201053020.png)

   

   

4. **定时任务（可选）：** 在任务菜单中创建定时任务，实现自动化操作。

![image-20250216201107320](C:\Users\kdx10\AppData\Roaming\Typora\typora-user-images\image-20250216201107320.png)

