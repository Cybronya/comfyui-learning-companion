---
name: unknown_workflow_video_sampler_clip_24
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.665125
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, PreviewImage, SetNode, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanMoeKSampler, WanVideoVACEStartToEndFrame, easy anythingIndexSwitch, easy int, easy positive, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1975438275764686849.json, 视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json, 视频生成/图生视频/2021413610848784385.json, 视频生成/图生视频/2043579993401335809.json, 视频生成/图生视频/2051204649931296770.json, 视频生成/图生视频/2051549317508411394.json, 视频生成/图生视频/2003774639149096961.json, 视频生成/图生视频/2003256917193555969.json, 视频生成/图生视频/2003260788590673922.json, 视频生成/图生视频/1996774154579976194.json, 视频生成/图生视频/1988562888287805442.json, 视频生成/图生视频/1996837849146302466.json, 视频生成/文生视频/Wan2.2官方：图生视频扩写长视频_2018279365133471745.json, 视频生成/文生视频/Wan2.2官方：视频扩写及图生视频工作流_2018624255843377154.json, 视频生成/文生视频/Wan2.2官方：视频扩写及图生视频工作流_2032046393744957441.json, 视频生成/文生视频/wan2.2-图生视频扩写--官方_2056643995220140034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1975438275764686849.json、视频生成/图生视频/wan2.2-Remix-ns-fw-官方视频-图生视频丝滑版_1986645790850510849.json、视频生成/图生视频/2021413610848784385.json、视频生成/图生视频/2043579993401335809.json、视频生成/图生视频/2051204649931296770.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `WanVideoVACEStartToEndFrame`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImpactFloat` —— 15/16 个有
- `Qwen3_VQA` —— 15/16 个有
- `WanImageToVideo` —— 15/16 个有
- `easy showAnything` —— 15/16 个有
- `LoraLoaderModelOnly` —— 14/16 个有
- `MathExpression|pysssss` —— 14/16 个有
- `MemoryCleaner` —— 14/16 个有
- `ModelBlockSwap` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `easy imageSize` —— 13/16 个有
- `CLIPVisionEncode` —— 3/16 个有
- `CLIPVisionLoader` —— 3/16 个有
- `ImageStitch` —— 2/16 个有
- `easy imageRemBg` —— 2/16 个有
- `CR Upscale Image` —— 1/16 个有
- `Float` —— 1/16 个有
- `Florence2ModelLoader` —— 1/16 个有
- `Florence2Run` —— 1/16 个有
- `PainterI2V` —— 1/16 个有
- `QwenLoader` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `SaveLatent` —— 1/16 个有
- `WanVideoPromptExtender` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 16 | 100% |
| 采样算法 | 1.5 | 1.5 - 1.5 | 16 | 100% |
| 调度器 | 1 | 1 - 1 | 16 | 100% |
| 重绘幅度 | sa_solver | - | 16 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，16 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1.5，观测区间 1.5 - 1.5，16 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，16 个样本，一致性 94%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
