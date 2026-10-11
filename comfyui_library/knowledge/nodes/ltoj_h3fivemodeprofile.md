# LtoJ_H3FiveModeProfile

## 节点类型

`LtoJ_H3FiveModeProfile`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `gpu:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `steps:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `quality_strategy:COMBO`（1 次）
- `reference_quality:COMBO`（1 次）

## 输出

- `宽:INT`（1 次）
- `高:INT`（1 次）
- `H3帧数:INT`（1 次）
- `质量步数:INT`（1 次）
- `选择秒数:INT`（1 次）
- `参考素材策略:STRING`（1 次）
- `生成计划:STRING`（1 次）
- `档位报告:STRING`（1 次）
- `运行档位:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["自动检测GPU", "5秒", "15步", "16:9 横屏", "768p（原生分辨率）", "测试视频", "标准（推荐）"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
