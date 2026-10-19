---
name: unknown_workflow_video_sampler_vae_10
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 1
common_nodes: [Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1927564692397383681.json, 视频生成/图生视频/1927226196612829186.json, 视频生成/图生视频/2018169625632055297.json, 视频生成/图生视频/1927627069877030914.json, 视频生成/图生视频/1927678754154528770.json, 视频生成/图生视频/1927606759882383362.json, 视频生成/图生视频/1940735459234627585.json, 视频生成/图生视频/1963630327368601601.json, 视频生成/图生视频/1963832271633616897.json, 视频生成/图生视频/1963826816140152833.json, 视频生成/图生视频/1963799539037736961.json, 视频生成/图生视频/1963808996464611329.json, 视频生成/图生视频/1940702520341671937.json, 视频生成/图生视频/1940706583401705474.json, 视频生成/图生视频/1914660971821105153.json, 视频生成/图生视频/1914643124784721922.json, 视频生成/图生视频/1940711079049670657.json, 视频生成/图生视频/1963821288294944770.json, 视频生成/图生视频/1940738830645489665.json, 视频生成/图生视频/1957783332476088321.json, 视频生成/图生视频/1940728388887932930.json, 视频生成/图生视频/2012898445341757442.json, 视频生成/图生视频/1933792108618633218.json, 视频生成/图生视频/1940731797691068417.json, 视频生成/图生视频/1965035525444915201.json, 视频生成/图生视频/1972553503535263745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/1927564692397383681.json、视频生成/图生视频/1927226196612829186.json、视频生成/图生视频/2018169625632055297.json、视频生成/图生视频/1927627069877030914.json、视频生成/图生视频/1927678754154528770.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 26 个 workflow 都包含：
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoClipTextEncoder` —— 25/26 个有
- `SimpleMath+` —— 25/26 个有
- `WanVideoImageClipEncode` —— 25/26 个有
- `DownloadAndLoadGIMMVFIModel` —— 24/26 个有
- `GIMMVFI_interpolate` —— 24/26 个有
- `LayerUtility: PurgeVRAM V2` —— 24/26 个有
- `Text Multiline` —— 19/26 个有
- `WanVideoEasyCache` —— 17/26 个有
- `WanVideoLoraSelectMulti` —— 17/26 个有
- `WanVideoLoraSelect` —— 9/26 个有
- `CR Text` —— 7/26 个有
- `ImageResizeKJ` —— 7/26 个有
- `RH_OneShot_Prompter` —— 3/26 个有
- `WanVideoMagCache` —— 3/26 个有
- `WanVideoVACEEncode` —— 1/26 个有
- `WanVideoVACEStartToEndFrame` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
