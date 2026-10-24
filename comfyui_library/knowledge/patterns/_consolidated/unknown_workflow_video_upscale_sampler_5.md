---
name: unknown_workflow_video_upscale_sampler_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9864
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageUpscaleWithModel, LoadImage, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json, 视频生成/图生视频/wanvideo首尾帧高清放大补针版_1912059507571392514.json, 视频生成/图生视频/墙绘转视频_1916826717670019073.json, 视频生成/图生视频/自拍转视频_1919610093690884097.json, 视频生成/图生视频/趴地转视频_1918873507273576450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.1单帧Wan2.1-Fun-InP-14B高清放大补针_1912093411476996097.json、视频生成/图生视频/wanvideo首尾帧高清放大补针版_1912059507571392514.json、视频生成/图生视频/墙绘转视频_1916826717670019073.json、视频生成/图生视频/自拍转视频_1919610093690884097.json、视频生成/图生视频/趴地转视频_1918873507273576450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoClipTextEncoder` —— 4/5 个有
- `TextInputBasic` —— 3/5 个有
- `WanVideoClipVisionEncode` —— 3/5 个有
- `WanVideoEnhanceAVideo` —— 3/5 个有
- `WanVideoImageToVideoEncode` —— 3/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `Bjornulf_FreeVRAM` —— 2/5 个有
- `Get resolution [Crystools]` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `LayerUtility: TextJoin` —— 2/5 个有
- `WanVideoImageClipEncode` —— 2/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `ImageResize+` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
