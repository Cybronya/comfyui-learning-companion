---
name: image_to_image_lora_sampler_clip_6
type: Image To Image
frequency: 19
level: strong
coverage: 0.858579
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json, 图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2100209388236660737.json, 图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2101877910243209218.json, 图片生成/图生图/Face Swap Pro换脸pro+2.0完美换脸+写实人物一致性_2097490583530070017.json, 图片生成/图生图/Face Swaps klein-9B 双图编辑 换脸换装_2100037705118867457.json, 图片生成/图生图/Face Swap完美换脸+写实人物一致性_2099675578382245890.json, 图片生成/图生图/Face_Swaps_klein-9B_双图编辑_换脸换装_2100423150663196674.json, 图片生成/图生图/试衣换装Flux Klein 9b Edit的虚拟试穿LoRA，超精确_2026645785999319041.json, 图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora +3种模式值之一 -- 2_2092660020956721153.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora_+3种模式值之一_--_2_2093496064706965505.json, 图片生成/图生图/超强图像一致性Flux2-Klein-9B-Consis-Lora_+3种模式值之一_--_2_2093534787322605569.json, 平台全量/Face_Swaps_klein-9B_双图编辑_换脸换装_2100871783531503617.json, 平台全量/Face_Swaps_klein-9B_双图编辑_换脸换装_2101138537323257858.json, 平台全量/完美无痕换脸  4k画质 换脸换头 自然换脸换脸换装多图编辑_2066749180479102978.json, 平台全量/换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170.json, 平台全量/换脸pro加强版+2.0完美换脸+写实人物一致性+全能图片+双图编辑 4K高清图像生成_2064607748033179650.json, 平台全量/无偏差不变色 最强换脸pro完美换脸全能图片 人物一致性 自然真实留细节_2067849337924841473.json, 平台全量/极致无痕换脸 自然换脸 4k画质 换脸换头 换脸换装多图编辑 脸部抠图_2066698432827453442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json、图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2100209388236660737.json、图片生成/图生图/Character_Head_and_Face_Swaps人物换头换脸_2101877910243209218.json、图片生成/图生图/Face Swap Pro换脸pro+2.0完美换脸+写实人物一致性_2097490583530070017.json、图片生成/图生图/Face Swaps klein-9B 双图编辑 换脸换装_2100037705118867457.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 19 个 workflow 都包含：
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
- `RH_Nano_Banana2_Image2Image` —— 14/19 个有
- `CR Text` —— 7/19 个有
- `ImageConcatMulti` —— 7/19 个有
- `MuyeTextEditOutput` —— 7/19 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 7/19 个有
- `CR Prompt Text` —— 3/19 个有
- `EmptyImage` —— 3/19 个有
- `PreviewImage` —— 3/19 个有
- `RH_SeedreamV5ProImageToImage` —— 3/19 个有
- `GetNode` —— 1/19 个有
- `SetNode` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 19 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，19 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（27/19 个样本）：Steps较低可能导致细节不足
