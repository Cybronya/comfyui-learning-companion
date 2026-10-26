---
name: unknown_workflow_video_lora_sampler_280
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.744
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkSilentEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/03-10-05-WAN2.1-数字人-百组动态无声长视频_1989933752463880193.json, 视频生成/图生视频/03-10-09-WAN2.1-无限时长分镜头控制-infinitetalk_2006714011445895170.json, 视频生成/图生视频/100秒长视频直出！Wan2.2超级魔改图生视频_1967041274844995586.json, 视频生成/图生视频/Wan+Inifinte Talk无限时长+动作分段控制视频生成（闭嘴版）_1968534429834588161.json, 视频生成/图生视频/大明动画风格 长视频 强制闭嘴_1970454402555408386.json, 视频生成/图生视频/（闭嘴版）Wan+Inifinte Talk无限时长+动作分段控制视频生成V1_1965504800706187266.json, 视频生成/图生视频/（非SVI）手搓Wan无限时长分镜头控制极速版图生视频V1_2005591443018317826.json, 音频生成/音频生成/数字人对口型Wan+Inifinte Talk无限时长_1967102112964468737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_280

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/03-10-05-WAN2.1-数字人-百组动态无声长视频_1989933752463880193.json、视频生成/图生视频/03-10-09-WAN2.1-无限时长分镜头控制-infinitetalk_2006714011445895170.json、视频生成/图生视频/100秒长视频直出！Wan2.2超级魔改图生视频_1967041274844995586.json、视频生成/图生视频/Wan+Inifinte Talk无限时长+动作分段控制视频生成（闭嘴版）_1968534429834588161.json、视频生成/图生视频/大明动画风格 长视频 强制闭嘴_1970454402555408386.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkSilentEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `JWInteger` —— 6/8 个有
- `GetNode` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `ConcatTextOfUtils` —— 1/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Primitive integer [Crystools]` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
