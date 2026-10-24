---
name: unknown_workflow_video_sampler_clip_83
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.98375
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/通义万相Teacache加速图生视频_1896425086226726914.json, 视频生成/图生视频/通义万相wan2.1万物生花特效_1908182289698664449.json, 视频生成/图生视频/通义万相wan2.1万物老化特效_1912458633853239298.json, 视频生成/图生视频/通义万相wan2.1图生视频万物婴儿化_1911273702397308929.json, 视频生成/图生视频/通义万相wan2.1图生视频万物放气特效_1910623040215154690.json, 视频生成/图生视频/通义万相wan2.1图生视频美女转身舞动_1910235144152674306.json, 视频生成/图生视频/通义万相wan2.1美女一字马_1909453938431504386.json, 视频生成/文生视频/火力 全开！冲锋枪射击特效--万相WAN2.1_1934071211976478722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/通义万相Teacache加速图生视频_1896425086226726914.json、视频生成/图生视频/通义万相wan2.1万物生花特效_1908182289698664449.json、视频生成/图生视频/通义万相wan2.1万物老化特效_1912458633853239298.json、视频生成/图生视频/通义万相wan2.1图生视频万物婴儿化_1911273702397308929.json、视频生成/图生视频/通义万相wan2.1图生视频万物放气特效_1910623040215154690.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 7/8 个有
- `GIMMVFI_interpolate` —— 7/8 个有
- `LayerUtility: PurgeVRAM` —— 7/8 个有
- `WanVideoLoraSelect` —— 7/8 个有
- `ImageResizeKJ` —— 6/8 个有
- `UpscaleModelLoader` —— 5/8 个有
- `CR Upscale Image` —— 3/8 个有
- `UpscaleImageByUsingModel` —— 3/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `ImageResize+` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
