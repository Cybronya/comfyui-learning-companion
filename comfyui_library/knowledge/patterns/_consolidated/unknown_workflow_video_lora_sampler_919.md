---
name: unknown_workflow_video_lora_sampler_919
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: ["视频生成/文生视频/DITTO-视频的极简转绘,一键吉卜力等多风格嵌套_1980577959260147714.json", 视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_919

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/DITTO-视频的极简转绘,一键吉卜力等多风格嵌套_1980577959260147714.json、视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `AddLabel` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WidgetToString` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
