---
name: unknown_workflow_video_lora_sampler_551
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.934
common_nodes: [CR Text, GetImageSizeAndCount, ImageFromBatch+, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json, 视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json, 视频生成/文生视频/Wan2.2文生视频KJ版（自动润饰提示词）_1950563765865598978.json, 视频生成/文生视频/Wan2.2文生视频添加背景音版_1951548166669807618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_551

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.2-SmoothMix-V2版 文生视频_1979793896198803458.json、视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json、视频生成/文生视频/Wan2.2文生视频KJ版（自动润饰提示词）_1950563765865598978.json、视频生成/文生视频/Wan2.2文生视频添加背景音版_1951548166669807618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/4 个有
- `GIMMVFI_interpolate` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `Wan_video_prompt_generator` —— 2/4 个有
- `MMAudioFeatureUtilsLoader` —— 1/4 个有
- `MMAudioModelLoader` —— 1/4 个有
- `MMAudioSampler` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
