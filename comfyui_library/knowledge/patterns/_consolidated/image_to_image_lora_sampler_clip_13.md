---
name: image_to_image_lora_sampler_clip_13
type: Image To Image
frequency: 12
level: strong
coverage: 0.8715
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json, 图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2100209388236660737.json, 图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2101877910243209218.json, 图片生成/图生图/Face Swap Pro换脸pro+2.0完美换脸+写实人物一致性_2097490583530070017.json, 图片生成/图生图/Face Swaps klein-9B 双图编辑 换脸换装_2100037705118867457.json, 图片生成/图生图/Face Swap完美换脸+写实人物一致性_2099675578382245890.json, 图片生成/图生图/Face_Swaps_klein-9B_双图编辑_换脸换装_2100423150663196674.json, 图片生成/图生图/试衣换装Flux Klein 9b Edit的虚拟试穿LoRA，超精确_2026645785999319041.json, 图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora +3种模式值之一 -- 2_2092660020956721153.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora_+3种模式值之一_--_2_2093496064706965505.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora_+3种模式值之一_--_2_2093534787322605569.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json、图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2100209388236660737.json、图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2101877910243209218.json、图片生成/图生图/Face Swap Pro换脸pro+2.0完美换脸+写实人物一致性_2097490583530070017.json、图片生成/图生图/Face Swaps klein-9B 双图编辑 换脸换装_2100037705118867457.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 7/12 个有
- `CR Text` —— 5/12 个有
- `ImageConcatMulti` —— 5/12 个有
- `CR Prompt Text` —— 3/12 个有
- `EmptyImage` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `RH_SeedreamV5ProImageToImage` —— 3/12 个有
- `MuyeTextEditOutput` —— 2/12 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 12 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，12 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（20/12 个样本）：Steps较低可能导致细节不足
