---
name: unknown_workflow_video_sampler_clip_93
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.940571
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan无限延长抽帧图生视频工作流_1894765811745816578.json, 视频生成/图生视频/压扁万物=艾橘溪_1899415401065828354.json, 视频生成/图生视频/变胖飞走+通义万相=艾橘溪_1900846163619389442.json, 视频生成/图生视频/捏捏乐+通义万相=艾橘溪_1900825368478261250.json, 视频生成/图生视频/最强视频开源模型-Wan2.1-360旋转_1900079206938587137.json, 视频生成/图生视频/通义万相之图片捏捏乐_1940715917842214913.json, 视频生成/图生视频/🦖wan2.1 变玩偶捏捏_1925461590995292161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan无限延长抽帧图生视频工作流_1894765811745816578.json、视频生成/图生视频/压扁万物=艾橘溪_1899415401065828354.json、视频生成/图生视频/变胖飞走+通义万相=艾橘溪_1900846163619389442.json、视频生成/图生视频/捏捏乐+通义万相=艾橘溪_1900825368478261250.json、视频生成/图生视频/最强视频开源模型-Wan2.1-360旋转_1900079206938587137.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Image Batch` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `WanVideoTorchCompileSettings` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
