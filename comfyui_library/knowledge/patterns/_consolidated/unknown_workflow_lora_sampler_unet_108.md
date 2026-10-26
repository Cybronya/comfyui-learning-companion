---
name: unknown_workflow_lora_sampler_unet_108
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.895143
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json, 图片生成/文生图/Qwen-Edit手机上的3D城市_2032281919450255362.json, 图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json, 图片生成/文生图/上传图片+手动输入提示词来生成下一场景+全节点注释_2055618848560295937.json, 图片生成/文生图/动作编辑器应用之四__FireRed文生图_2021382520541028354.json, 图片生成/文生图/换装同服装双人或者多人同框_1994237410244493314.json, 数字人/数字人/KYLIN_2509 (IP角色编辑)_1983015644268507137.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_108

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json、图片生成/文生图/Qwen-Edit手机上的3D城市_2032281919450255362.json、图片生成/文生图/Qwen-Image Edit Plus换装双人同框_1994201692587622402.json、图片生成/文生图/上传图片+手动输入提示词来生成下一场景+全节点注释_2055618848560295937.json、图片生成/文生图/动作编辑器应用之四__FireRed文生图_2021382520541028354.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 6/7 个有
- `EmptyLatentImage` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `BiRefNetRMBG` —— 2/7 个有
- `ConstrainImage|pysssss` —— 2/7 个有
- `LayerUtility: ExtendCanvas` —— 2/7 个有
- `CR Latent Input Switch` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `EmptySD3LatentImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 1024 - 1920 | 6 | 74% |
| 高度 | 1408 | 720 - 1920 | 6 | 71% |
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 1024 - 1920，6 个样本
- 高度 中位数 1408，观测区间 720 - 1920，6 个样本
- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
