---
name: image_to_image_sampler_vae_32
type: Image To Image
frequency: 4
level: strong
coverage: 0.92325
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToMegapixels, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_2052751252513148930.json, 图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json, 平台全量/【光速版】Qwen Image EDIT 人物一致多角度  美女模特人物不同视角 IP角色创建_1969551977065684993.json, 数字人/数字人/双节棍版光速Qwen Image EDIT工作流_2053129289540874242.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/双节棍版光速Qwen Image EDIT工作流_2052751252513148930.json、图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json、平台全量/【光速版】Qwen Image EDIT 人物一致多角度  美女模特人物不同视角 IP角色创建_1969551977065684993.json、数字人/数字人/双节棍版光速Qwen Image EDIT工作流_2053129289540874242.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有
- `TextInputNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.6 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
