# WujiDirector

## 节点类型

`WujiDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `助力源:WUJI_LLM`（2 次）
- `核心情节输入:STRING`（2 次）
- `视频时长:COMBO`（2 次）
- `导演风格:COMBO`（2 次）
- `时代设定:COMBO`（2 次）
- `视觉艺术流派:COMBO`（2 次）
- `信念模式:BOOLEAN`（2 次）
- `手动分镜数:INT`（2 次）
- `自定分镜指令:STRING`（2 次）

## 输出

- `魔改剧本:STRING`（2 次）
- `风格配置:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["小红帽的故事", "🎬 短视频(15秒)", "自动", "自动", "自动", false, 0, ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
