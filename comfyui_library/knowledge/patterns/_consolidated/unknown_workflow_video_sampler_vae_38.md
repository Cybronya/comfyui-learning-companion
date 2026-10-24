---
name: unknown_workflow_video_sampler_vae_38
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9967
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强FusionX图生视频_1935158356237557762.json, 图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json, 图片生成/文生图/最强FusionX文生视频_1935149861173927937.json, 视频生成/图生视频/Self-Forcing-VACE图生视频极速版_1935716384242659330.json, 视频生成/图生视频/Wan2.1-FusionX-VACE图生视频_1934805890510069762.json, 视频生成/图生视频/Wan2.1-FusionX-VACE图生视频加速工作流_1935618594950807553.json, 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频_1935624058308317186.json, 视频生成/图生视频/Wan2.1-VACE+FusionX-LORA图生视频工作流_1937018239794974722.json, 视频生成/图生视频/moviigen+vace+accvid极速图生视频+补帧放大_1924274970828918785.json, 视频生成/图生视频/万相win2.1+ VACE首尾帧+accvid加速+2倍补帧流畅  生成最终帧率30，保证流畅_1928305949314793473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/最强FusionX图生视频_1935158356237557762.json、图片生成/文生图/Wan2.1-FusionX文生视频_1933717889453350913.json、图片生成/文生图/最强FusionX文生视频_1935149861173927937.json、视频生成/图生视频/Self-Forcing-VACE图生视频极速版_1935716384242659330.json、视频生成/图生视频/Wan2.1-FusionX-VACE图生视频_1934805890510069762.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 9/10 个有
- `WanVideoTeaCache` —— 9/10 个有
- `LoadImage` —— 8/10 个有
- `Primitive integer [Crystools]` —— 8/10 个有
- `Text Multiline` —— 8/10 个有
- `WanVideoVACEEncode` —— 8/10 个有
- `WanVideoVACEStartToEndFrame` —— 8/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/10 个有
- `GIMMVFI_interpolate` —— 4/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `WanVideoVACEModelSelect` —— 4/10 个有
- `ImageResizeKJ` —— 3/10 个有
- `JWInteger` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `CR Upscale Image` —— 2/10 个有
- `Int` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `WanVideoEmptyEmbeds` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `ImageRepeat` —— 1/10 个有
- `String Literal` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
