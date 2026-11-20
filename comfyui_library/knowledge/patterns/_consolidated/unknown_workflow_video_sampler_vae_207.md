---
name: unknown_workflow_video_sampler_vae_207
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.919
common_nodes: [AILab_QwenVL, GetImageRangeFromBatch, INTConstant, ImageResizeKJv2, Textbox, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/03-SkyReelsV3_V2V Shot-视频角度切换工作流_2029227388466372610.json, 平台全量/01-Skyreel_v3_V2V_视频循环扩展工作流_2029151504791244801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_207

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/03-SkyReelsV3_V2V Shot-视频角度切换工作流_2029227388466372610.json、平台全量/01-Skyreel_v3_V2V_视频循环扩展工作流_2029151504791244801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `GetImageRangeFromBatch`
- `INTConstant`
- `ImageResizeKJv2`
- `Textbox`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
