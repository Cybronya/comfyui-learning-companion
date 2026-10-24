# ImageURLLoader

## 节点类型

`ImageURLLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `imgurl:STRING`（5 次）
- `error_message:STRING`（5 次）
- `throw_error:BOOLEAN`（5 次）

## 输出

- `图像列表:IMAGE`（5 次）
- `报错显示:STRING`（5 次）
- `有效图像链接数量:STRING`（5 次）
- `输入端imgurl图像链接总数量:STRING`（5 次）
- `有效图像链接:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["http://aigccdn.hzaiyue.com/project/33/role/652_0.jpg", "未找到有效的图像链接", false]`（1 次）
- `["https://xiaotu-test-cos.pinstyles.cn/1983365511518691330/1983366562300895233/user/temp/crop-1762746168529.png", "未找到有效`（1 次）
- `["https://xiaotu-test-cos.pinstyles.cn/1983365511518691330/1983366562300895233/user/temp/crop-1762754505504.png", "未找到有效`（1 次）
- `["https://xiaotu-test-cos.pinstyles.cn/1983365511518691330/1983366562300895233/user/temp/output-blackwhite-347503.png", `（1 次）
- `["https://cloud.mianliaoyinxiang.com/image/1768374893710_hd_1768374893707_ComfyUI_00152_.png?imageMogr2/thumbnail/400x/f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
