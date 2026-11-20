---
name: unknown_workflow_video_lora_sampler_261
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.900444
common_nodes: [CLIPVisionLoader, LoadImage, SplineEditor, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WanMove图生视频动作编辑_1999827613361242114.json, 视频生成/图生视频/Wanmove_轨迹运动_图生视频_1999179098159185922.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999117926080933890.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999366459300212737.json, 视频生成/图生视频/Wanmove多点轨迹运动指引图生视频V1_1999110831537258497.json, 视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2007470369120198658.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2008000096457203714.json, 视频生成/文生视频/Wan-Move潜在轨迹引导视频生成_1998898965116542977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_261

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/WanMove图生视频动作编辑_1999827613361242114.json、视频生成/图生视频/Wanmove_轨迹运动_图生视频_1999179098159185922.json、视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999117926080933890.json、视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999366459300212737.json、视频生成/图生视频/Wanmove多点轨迹运动指引图生视频V1_1999110831537258497.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoAddWanMoveTracks`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 8/9 个有
- `RepeatImageBatch` —— 8/9 个有
- `WanVideoSetBlockSwap` —— 8/9 个有
- `WanVideoSetLoRAs` —— 8/9 个有
- `WanVideoTextEncode` —— 8/9 个有
- `WanVideoWanDrawWanMoveTracks` —— 8/9 个有
- `INTConstant` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `WanVideoTorchCompileSettings` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `ImageConcanate` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `WanVideoTextEncodeCached` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
