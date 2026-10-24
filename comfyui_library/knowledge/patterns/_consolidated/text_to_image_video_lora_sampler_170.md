---
name: text_to_image_video_lora_sampler_170
type: Text To Image
frequency: 3
level: strong
coverage: 0.919667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, EmptyLatentImage, JjkText, KSampler, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MAGREF吻屏互动图生视频｜人物特效角色设计｜隔屏亲吻名场面生成_2104787978848661506.json, 视频生成/图生视频/MAGREF吻屏图生视频｜人物类特效角色设计｜亲亲互动视频轻松做_2104922636890492930.json, 视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_170

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MAGREF吻屏互动图生视频｜人物特效角色设计｜隔屏亲吻名场面生成_2104787978848661506.json、视频生成/图生视频/MAGREF吻屏图生视频｜人物类特效角色设计｜亲亲互动视频轻松做_2104922636890492930.json、视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `AppendStringsToList` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `SplineEditor` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `WanVideoATITracks` —— 1/3 个有
- `WanVideoATITracksVisualize` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
