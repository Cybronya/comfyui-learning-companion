# RH_BytedanceSeedance20GlobalMiniMultimodalVideo

## 节点类型

`RH_BytedanceSeedance20GlobalMiniMultimodalVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `image6:IMAGE`（3 次）
- `image7:IMAGE`（3 次）
- `image8:IMAGE`（3 次）
- `image9:IMAGE`（3 次）
- `video1:VIDEO`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dance", "480p", "4", true, "adaptive", true, "all", false, 250291421, "randomize", false]`（1 次）
- `["Image1 角色按照video1运镜展示，画面风格与image1保持一致", "480p", "4", true, "16:9", true, "all", false, 1003766217, "randomize", false]`（1 次）
- `["通用开场白（适用于所有商家）\n（小陈面带微笑背着背包，走进店内，主动打招呼）\n小陈：老板好！打扰一下，我是做智能收银系统推广的，方便占用您一两分钟时间吗？\n老板：你是干嘛的？\n小陈：我是银豹科技的，专门给咱商家提供智能收银系统。`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
