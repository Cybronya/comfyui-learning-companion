# Wan_video_prompt_generator

## 节点类型

`Wan_video_prompt_generator`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `语言:COMBO`（1 次）
- `用户提示词:STRING`（1 次）
- `镜头大小:COMBO`（1 次）
- `灯光类型:COMBO`（1 次）
- `光源:COMBO`（1 次）
- `色调:COMBO`（1 次）
- `摄像机角度:COMBO`（1 次）
- `镜头:COMBO`（1 次）
- `基础摄像机运动:COMBO`（1 次）
- `高级摄像机运动:COMBO`（1 次）

## 输出

- `generated_prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["zh", "美丽的秦国古风女人，身穿红衣，头发扎了起来，碎发被风吹动，她低下头，表情十分沮丧，眼角有泪痕", "中景", "柔光", "阳光", "暖色调", "俯视角度", "广角镜头", "拉远", "无", "蓝调时刻", "无"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
