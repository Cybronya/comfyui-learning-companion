---
name: unknown_workflow_video_sampler_vae_141
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88875
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商多图参考生成视频 skyreel V3_2017384271350075393.json, 平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json, 视频生成/图生视频/SkyReels V3多图参考大模型：上传两张人物照生成合拍视频！_2017184716553719810.json, 视频生成/图生视频/多图合成视频工作流_2019122277626941442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/电商多图参考生成视频 skyreel V3_2017384271350075393.json、平台全量/Wan21_FusionX_PhantomWFv2_Y_Workflow_1934801211566530561.json、视频生成/图生视频/SkyReels V3多图参考大模型：上传两张人物照生成合拍视频！_2017184716553719810.json、视频生成/图生视频/多图合成视频工作流_2019122277626941442.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoSetLoRAs` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
