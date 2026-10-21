---
name: unknown_workflow_video_lora_sampler_698
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.972
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/1951554035532902402.json, 视频生成/文生视频/1950563765865598978.json, 视频生成/文生视频/1951548166669807618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_698

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1951554035532902402.json、视频生成/文生视频/1950563765865598978.json、视频生成/文生视频/1951548166669807618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageFromBatch+` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `ImpactSwitch` —— 1/3 个有
- `MMAudioFeatureUtilsLoader` —— 1/3 个有
- `MMAudioModelLoader` —— 1/3 个有
- `MMAudioSampler` —— 1/3 个有
- `SeargePromptText` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `Wan_video_prompt_generator` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
