---
name: unknown_workflow_sampler_clip_unet_37
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.903667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1989200631200100353.json, 图片生成/文生图/1994260229521162241.json, 图片生成/文生图/251207-02.Z_image_turbo文生图_1997679556008022018.json, 图片生成/文生图/3D盲盒潮玩手办-文生图_2094262553378648065.json, 图片生成/文生图/60.tonnie-Magic-Wan-Image文生图_2009063719375998977.json, 图片生成/文生图/90后动漫风格-ZImage文生图_2018945323267268610.json, 图片生成/文生图/DreamCore-梦核_2073300420767862785.json, 图片生成/文生图/Qwen-image-2512 文生图_2009132641324376066.json, 图片生成/文生图/Z-Image-Turbo批量文生图_1993884946834145281.json, 图片生成/文生图/Z-Image文生图_2007450236398084098.json, 图片生成/文生图/Z-image 文生图_2017213414262710273.json, 图片生成/文生图/动漫出图Qwen工作流_2019691912264945666.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1989200631200100353.json、图片生成/文生图/1994260229521162241.json、图片生成/文生图/251207-02.Z_image_turbo文生图_1997679556008022018.json、图片生成/文生图/3D盲盒潮玩手办-文生图_2094262553378648065.json、图片生成/文生图/60.tonnie-Magic-Wan-Image文生图_2009063719375998977.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 9/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `PrimitiveStringMultiline` —— 4/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `StringFunction|pysssss` —— 2/12 个有
- `easy promptLine` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `LoraLoader` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 11 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
