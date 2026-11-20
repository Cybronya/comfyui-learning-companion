---
name: unknown_workflow_video_lora_sampler_454
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6864
common_nodes: [CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageFromBatch+, Int, JWStringConcat, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_LLMAPI_NODE, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json, 视频生成/文生视频/Wan 2.2 文本到视频广告_1950092714999201793.json, 视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json, 视频生成/文生视频/Wan+2.2创意开箱视频广告_1951952632132874241.json, 视频生成/文生视频/Wan2.2创意开箱视频广告_1960890103814139905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_454

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Wan+2.2创意开箱视频广告_2058721201614319618.json、视频生成/文生视频/Wan 2.2 文本到视频广告_1950092714999201793.json、视频生成/文生视频/Wan+2.2+文本到视频广告_1951940652722540546.json、视频生成/文生视频/Wan+2.2创意开箱视频广告_1951952632132874241.json、视频生成/文生视频/Wan2.2创意开箱视频广告_1960890103814139905.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
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
- `JsonToText` —— 4/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
