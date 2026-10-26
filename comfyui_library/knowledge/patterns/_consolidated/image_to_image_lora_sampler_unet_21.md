---
name: image_to_image_lora_sampler_unet_21
type: Image To Image
frequency: 18
level: strong
coverage: 0.795444
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 2511一键96个分镜图_2026570422766018562.json, 图片生成/图生图/Qwen-Edit-2511-多图编辑_2003681947601805313.json, 图片生成/图生图/Qwen-image-edit2511-风格多样化 创意玩法_2010195628764176385.json, 图片生成/图生图/Qwen-image-edit2511：创意变色龙！一张底图，指尖轻点解锁数十种风格_2010011563326967809.json, 图片生成/图生图/image2，gemini2，Qwen2511文字生成对比_2049381140200427521.json, 图片生成/图生图/qwen 2511 DFL补角度专用 99种角度 12种表情 总计1188张素材_2090830266335055873.json, 图片生成/图生图/一键生成96个分镜图+多角度=Multiple angles Qwen edit 2511_2009138997611728898.json, 图片生成/图生图/一键生成96个分镜图+多角度=Multiple angles Qwen edit 2511_2016818211605450754.json, 图片生成/图生图/一键生成几十张分镜图Qwen+edit+2511-打包zip_2010994201273569282.json, 图片生成/图生图/一键生成多个分镜图Qwen edit 2511-压缩包一次下载_2010894656611033090.json, 图片生成/图生图/一键生成多个分镜图多角度（最大96）_2030651649445863425.json, 图片生成/图生图/人物模特多角度 zip打包 生成96个分镜图 Multiple Qwen edit 2511！_2087070956895432706.json, 图片生成/图生图/千问edit2511：创意变色龙解锁数十种风格26127_2016127266601832449.json, 图片生成/图生图/单图出十二分镜超强一致_2027074826434781185.json, 图片生成/图生图/多角度人物多角度多场景Qwen-multiple-angles版_2059528095010480130.json, 图片生成/图生图/多角度人物多角度多场景Qwen-multiple-angles版_2059928373580877826.json, 图片生成/图生图/模特12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2061085110698594305.json, 图片生成/图生图/超好用🔥12种镜头场景生成多角度人物-ai动漫短剧_2057338973592317953.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen edit 2511一键96个分镜图_2026570422766018562.json、图片生成/图生图/Qwen-Edit-2511-多图编辑_2003681947601805313.json、图片生成/图生图/Qwen-image-edit2511-风格多样化 创意玩法_2010195628764176385.json、图片生成/图生图/Qwen-image-edit2511：创意变色龙！一张底图，指尖轻点解锁数十种风格_2010011563326967809.json、图片生成/图生图/image2，gemini2，Qwen2511文字生成对比_2049381140200427521.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 16/18 个有
- `INTConstant` —— 15/18 个有
- `LayerUtility: PurgeVRAM` —— 13/18 个有
- `easy promptLine` —— 13/18 个有
- `Text` —— 11/18 个有
- `HAIGC_SaveImagesToZip` —— 8/18 个有
- `GetNode` —— 7/18 个有
- `SetNode` —— 7/18 个有
- `PlaySound|pysssss` —— 5/18 个有
- `PreviewImage` —— 4/18 个有
- `MultiTextConcatenate` —— 3/18 个有
- `easy anythingIndexSwitch` —— 3/18 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/18 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 18 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 18 | 78% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，18 个样本
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
