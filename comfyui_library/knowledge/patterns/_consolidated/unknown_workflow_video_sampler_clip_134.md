---
name: unknown_workflow_video_sampler_clip_134
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.99
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json, 视频生成/图生视频/WAN2.1 抖音小红书快手网红跳舞视频_1946216750084186114.json, 视频生成/图生视频/Wan2.1 图生视频  低配无压力_1905875361152815105.json, 视频生成/图生视频/wan2.1 图生视频工作流(可本地调用)_1913664774507327490.json, 视频生成/图生视频/【女团跳舞】摇摆舞｜图生视频 超级高清_1913149294990557186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json、视频生成/图生视频/WAN2.1 抖音小红书快手网红跳舞视频_1946216750084186114.json、视频生成/图生视频/Wan2.1 图生视频  低配无压力_1905875361152815105.json、视频生成/图生视频/wan2.1 图生视频工作流(可本地调用)_1913664774507327490.json、视频生成/图生视频/【女团跳舞】摇摆舞｜图生视频 超级高清_1913149294990557186.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `easy int` —— 2/5 个有
- `GetImageSize+` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WanVideoExperimentalArgs` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
