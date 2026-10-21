---
name: image_to_image_lora_sampler_clip_7
type: Image To Image
frequency: 4
level: strong
coverage: 0.832
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1988906774222737410.json, 图片生成/文生图/1989153552679448577.json, 图片生成/文生图/1989155186948059137.json, 图片生成/文生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2004037122640257026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1988906774222737410.json、图片生成/文生图/1989153552679448577.json、图片生成/文生图/1989155186948059137.json、图片生成/文生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2004037122640257026.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 3/4 个有
- `ControlNetInpaintingAliMamaApply` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PDImageResizeV2` —— 2/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 4 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，4 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
