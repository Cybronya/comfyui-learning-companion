---
name: image_to_image_sampler_clip_vae_15
type: Image To Image
frequency: 12
level: strong
coverage: 0.884667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json, 图片生成/图生图/Flux1 Kontext 去除图片水印_1968539542431125506.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku加速_1948148937090838529.json, 图片生成/图生图/Flux1-Kontext移除物品+修复-Nun加速_1949274803111436290.json, 图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json, 图片生成/图生图/kontext+LLM提示词优化+nunchaku加速工作流_1939506026280566785.json, 图片生成/图生图/kontext开源+LLM提示词优化+8步出图—用嘴改图开源模型单图王炸全能工作流_1939280801999593473.json, 图片生成/图生图/kontext老照片修复—用嘴改图开源模型单图模式_1938786627152236545.json, 图片生成/图生图/kontext高清放大（人像专用保持人像完全一致）_1939303624373673986.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json、图片生成/图生图/Flux1 Kontext 去除图片水印_1968539542431125506.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json、图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuFluxDiTLoader` —— 9/12 个有
- `RH_Translator` —— 9/12 个有
- `ShowText|pysssss` —— 8/12 个有
- `NunchakuFluxLoraLoader` —— 7/12 个有
- `Text Multiline` —— 7/12 个有
- `ImageStitch` —— 6/12 个有
- `RH_LLMAPI_NODE` —— 6/12 个有
- `CR Text` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `Int` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `UNETLoader` —— 3/12 个有
- `easy compare` —— 3/12 个有
- `easy ifElse` —— 3/12 个有
- `ImageConcanate` —— 2/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `ttN concat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 12 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
