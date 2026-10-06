# Krea2EditGroundedEncode

## 节点类型

`Krea2EditGroundedEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `image:IMAGE`（4 次）
- `image_b:IMAGE`（4 次）
- `prompt:STRING`（4 次）
- `grounding_px:INT`（4 次）
- `system_prompt:STRING`（4 次）

## 输出

- `CONDITIONING:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 768, ""]`（2 次）
- `["Change her outfit to a red raincoat.", 768, ""]`（1 次）
- `["由于目前环境盗工作流的蠢狗太多，所以隐藏提示词，\n有需求+VX：505642710（注明来意），闲人夹心的个人主页 https://www.runninghub.cn/user-center/1939682272276611073/w`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
