---
name: image_to_image_lora_sampler_vae_7
type: Image To Image
frequency: 12
level: strong
coverage: 0.860083
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键场景多视角分镜生成（九图）_2028269051671220226.json, 图片生成/图生图/图生多图_2039589422538170369.json, 图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版(3)_2105575602534313985.json, 图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版(3)_2108013564198998018.json, 图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版_2015789127156899841.json, 图片生成/图生图/场景多角度分镜制作镜头风格一致性_2034582009992974337.json, 图片生成/图生图/场景多角度分镜制作镜头风格一致性分镜_1985653251741757442.json, 图片生成/图生图/场景多角度分镜制作镜头风格一致性分镜加速版_1986327391331123201.json, 图片生成/图生图/场景多角度分镜制作镜头风格一致性分镜加速版_2054371399103459329.json, 图片生成/图生图/漫剧场景多视角生成_一键九图_2014219506553458689.json, 图片生成/图生图/漫剧场景多视角生成_一键九图_2037872634418958338.json, 平台全量/QwenEdit2511风格一致性多角度分镜生成_2036000282089361410.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/一键场景多视角分镜生成（九图）_2028269051671220226.json、图片生成/图生图/图生多图_2039589422538170369.json、图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版(3)_2105575602534313985.json、图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版(3)_2108013564198998018.json、图片生成/图生图/场景多角度分镜2.0制作镜头qwen2511风格一致性分镜加速版_2015789127156899841.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 11/12 个有
- `UNETLoader` —— 9/12 个有
- `Anything Everywhere3` —— 8/12 个有
- `Text Multiline` —— 7/12 个有
- `JjkText` —— 5/12 个有
- `EnhancedLoadDiffusionModel` —— 3/12 个有
- `ModelSamplingAuraFlow` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `Qwen3VLAPINode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 12 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | sa_solver | - | 12 | 67% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
