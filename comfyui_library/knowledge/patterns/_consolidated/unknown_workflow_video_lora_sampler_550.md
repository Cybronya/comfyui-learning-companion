---
name: unknown_workflow_video_lora_sampler_550
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.618
common_nodes: [CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageFromBatch+, Int, JWStringConcat, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_LLMAPI_NODE, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy seed, easy showAnything]
problems: []
missing: [ImageFromBatch+, MathExpression|pysssss, easy anythingIndexSwitch, easy cleanGpuUsed, easy seed]
members: [视频生成/文生视频/1951940652722540546.json, 视频生成/文生视频/1951952632132874241.json, 视频生成/文生视频/1950092714999201793.json, 视频生成/文生视频/1960890103814139905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_550

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1951940652722540546.json、视频生成/文生视频/1951952632132874241.json、视频生成/文生视频/1950092714999201793.json、视频生成/文生视频/1960890103814139905.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageFromBatch+`
- `Int`
- `JWStringConcat`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
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
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JsonToText` —— 3/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、MathExpression|pysssss、easy anythingIndexSwitch、easy cleanGpuUsed、easy seed
