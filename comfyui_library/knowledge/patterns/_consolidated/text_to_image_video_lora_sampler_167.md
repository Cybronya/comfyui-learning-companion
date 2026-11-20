---
name: text_to_image_video_lora_sampler_167
type: Text To Image
frequency: 4
level: strong
coverage: 0.89775
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateCFGScheduleFloatList, EmptyLatentImage, GetImageSizeAndCount, INTConstant, ImageFromBatch, JWInteger, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, RHHiddenNodes, RH_LLMAPI_Pro_Node, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy boolean, easy forLoopEnd, easy forLoopStart, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动态表情包滤镜特效创意形象图生视频_2087416229165355009.json, 视频生成/图生视频/动态表情包生成｜滤镜特效创意形象图生视频_2092382929543589889.json, 视频生成/图生视频/图生视频一键制作动态表情包，创意形象自带滤镜特效_2110435574405492737.json, 视频生成/图生视频/图生视频一键制作动态表情包，创意形象自带滤镜特效_2114183955657351169.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/动态表情包滤镜特效创意形象图生视频_2087416229165355009.json、视频生成/图生视频/动态表情包生成｜滤镜特效创意形象图生视频_2092382929543589889.json、视频生成/图生视频/图生视频一键制作动态表情包，创意形象自带滤镜特效_2110435574405492737.json、视频生成/图生视频/图生视频一键制作动态表情包，创意形象自带滤镜特效_2114183955657351169.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch`
- `JWInteger`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy boolean`
- `easy forLoopEnd`
- `easy forLoopStart`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
