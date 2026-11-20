---
name: unknown_workflow_sampler_clip_unet_102
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.94225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-4采极致细节_2044603720377311233.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2037904618847473665.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072122771399864322.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072127037019611138.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2072848197558554626.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2077553813770293249.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2077559193019699201.json, 图片生成/文生图/Z-Image-turb随机性出图多张_2081938785293651969.json, 图片生成/文生图/Z-image，文生图_2009572089073766402.json, 图片生成/文生图/krea2文生图二采放大_2078759847776051201.json, 图片生成/文生图/krea2文生图二采放大_2115619326089842690.json, 图片生成/文生图/krea2文生图二采放大_2115667146461245441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-4采极致细节_2044603720377311233.json、图片生成/文生图/Z-Image-turb随机性出图多张_2037904618847473665.json、图片生成/文生图/Z-Image-turb随机性出图多张_2072122771399864322.json、图片生成/文生图/Z-Image-turb随机性出图多张_2072127037019611138.json、图片生成/文生图/Z-Image-turb随机性出图多张_2072848197558554626.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `Int` —— 8/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `LatentUpscaleBy` —— 3/12 个有
- `ComfySwitchNode` —— 2/12 个有
- `ResolutionSelector` —— 2/12 个有
- `CR Seed` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `ttN text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 12 | 65% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 92% |
| 宽度 | 1536 | 1080 - 2064 | 12 | 84% |
| 高度 | 2048 | 720 - 2048 | 12 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，12 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 92%
- 宽度 中位数 1536，观测区间 1080 - 2064，12 个样本，取值集中（一致性 84%）
- 高度 中位数 2048，观测区间 720 - 2048，12 个样本
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
