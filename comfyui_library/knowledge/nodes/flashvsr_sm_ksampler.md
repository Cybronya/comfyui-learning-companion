# FlashVSR_SM_KSampler

## 节点类型

`FlashVSR_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:FlashVSR_SM_Model`（7 次）
- `image:IMAGE`（7 次）
- `width:INT`（7 次）
- `height:INT`（7 次）
- `seed:INT`（7 次）
- `scale:INT`（7 次）
- `kv_ratio:FLOAT`（7 次）
- `local_range:INT`（7 次）
- `steps:INT`（7 次）
- `cfg:FLOAT`（7 次）

## 输出

- `images:IMAGE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1280, 768, 1883416690, "randomize", 2, 3.5, 11, 1, 1, 2, true, true, "wavelet", 81]`（2 次）
- `[1280, 768, 1347591167, "randomize", 2, 3.5, 11, 1, 1, 2, true, true, "wavelet", 81]`（2 次）
- `[1280, 768, 2095198850, "randomize", 2, 3.5, 11, 1, 1, 2, true, true, "wavelet", 81]`（2 次）
- `[1280, 768, 424095978, "randomize", 2, 3.5, 11, 1, 1, 2, true, true, "wavelet", 81]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
