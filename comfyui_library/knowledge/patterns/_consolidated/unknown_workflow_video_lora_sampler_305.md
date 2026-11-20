---
name: unknown_workflow_video_lora_sampler_305
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.840333
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json, 平台全量/Wan-Move大模型：引导AI视频主角运动轨迹_2000121123553542146.json, 平台全量/Wan-Move潜在轨迹引导视频_2005604784524718081.json, 平台全量/wanmove视频控制_1999343954824921089.json, 数字人/数字人/Wanmove轨迹控制运动_1999275955468238849.json, 视频生成/图生视频/03-19-01-WAN2.1-扭曲艺术-Wanmove+Fill Nodes动与静轨迹控制_2000440766998736897.json, 视频生成/图生视频/Wan move指定轨迹运动-指引-图生视频版本1_1999398013804179457.json, 视频生成/图生视频/Wan-Move轨迹控制运动_2015351351290630146.json, 视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_305

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json、平台全量/Wan-Move大模型：引导AI视频主角运动轨迹_2000121123553542146.json、平台全量/Wan-Move潜在轨迹引导视频_2005604784524718081.json、平台全量/wanmove视频控制_1999343954824921089.json、数字人/数字人/Wanmove轨迹控制运动_1999275955468238849.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoAddWanMoveTracks`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoWanDrawWanMoveTracks`

**可变部分**（部分 workflow 才有）：
- `RepeatImageBatch` —— 8/9 个有
- `SplineEditor` —— 8/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `WanVideoTorchCompileSettings` —— 5/9 个有
- `INTConstant` —— 4/9 个有
- `ImageConcanate` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `FL_PathAnimator` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `SimpleMath+` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `CR Multiline Text` —— 1/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `Getter` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `Setter` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
