---
name: text_to_image_sampler_clip_unet_223
type: Text To Image
frequency: 2
level: weak
coverage: 0.718
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR Text, ClownsharKSampler_Beta, EmptyLatentImage, GetNode, Image Comparer (rgthree), KSampler, RunningHub SeedXPro Translator, SDXLEmptyLatentSizePicker+, SaveImage, Seed_, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat, easy showAnything, image_scale_pixel_v2]
problems: []
missing: []
members: [图片生成/文生图/【阿良绘】Anima3文生图 _ 参考图+自动化提示词_2043938725066973185.json, 图片生成/文生图/【阿良绘】Anima3文生图 _ 高质动漫生图（新）_2043956981622378497.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_223

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【阿良绘】Anima3文生图 _ 参考图+自动化提示词_2043938725066973185.json、图片生成/文生图/【阿良绘】Anima3文生图 _ 高质动漫生图（新）_2043956981622378497.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ClownsharKSampler_Beta`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `RunningHub SeedXPro Translator`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Seed_`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`
- `easy showAnything`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | normal | - | 2 | 50% |
| Prompt 约束强度(CFG) | 30 | - | 2 | 100% |
| 采样算法 | -1 | - | 2 | 100% |
| 调度器 | 0.9 | - | 2 | 89% |
| 重绘幅度 | 3 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 normal，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 重绘幅度 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
