---
name: unknown_workflow_video_sampler_clip_36
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.92875
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/扭扭弹弹跳舞_1904411310740905985.json, 图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json, 视频生成/图生视频/3D旋转+360度环旋+通义万相=艾橘溪_1900145552707809282.json, 视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json, 视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894658014006390785.json, 视频生成/图生视频/wan2.1图生视频，更新快速节点_1896816638631550978.json, 视频生成/图生视频/wan图生视频+超高清补帧_1903839569089826817.json, 视频生成/图生视频/特效合集，wan2.1图生视频，加速高清版_1899713009114107905.json, 视频生成/图生视频/🦖wan2.1图生视频(更新至0325)高清修复+lora修复_1894935249389039617.json, 视频生成/图生视频/🦖大风车转呀转_1932255495774437378.json, 视频生成/图生视频/🦖浪花特效_1930816773925306370.json, 视频生成/文生视频/wan图生视频+超高清补帧_1904728293755813889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/扭扭弹弹跳舞_1904411310740905985.json、图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json、视频生成/图生视频/3D旋转+360度环旋+通义万相=艾橘溪_1900145552707809282.json、视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json、视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894658014006390785.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `LayerUtility: PurgeVRAM` —— 9/12 个有
- `WanVideoLoraSelect` —— 9/12 个有
- `ImageUpscaleWithModel` —— 7/12 个有
- `RIFE VFI` —— 7/12 个有
- `UpscaleModelLoader` —— 7/12 个有
- `WanVideoEnhanceAVideo` —— 7/12 个有
- `WanVideoTeaCache` —— 7/12 个有
- `ImageResizeAdvanced` —— 5/12 个有
- `Int` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `TextInput_` —— 3/12 个有
- `WanVideoEmptyEmbeds` —— 3/12 个有
- `Text Multiline` —— 2/12 个有
- `WanVideoSLG` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `ImageResizeKJ` —— 1/12 个有
- `Note _O` —— 1/12 个有
- `ResizeLongestToNode` —— 1/12 个有
- `SaveLatent` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
