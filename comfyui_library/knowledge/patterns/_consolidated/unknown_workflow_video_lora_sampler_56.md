---
name: unknown_workflow_video_lora_sampler_56
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.9657
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2018039225307893762.json, 视频生成/图生视频/1979808803409530882.json, 视频生成/图生视频/2053339197372674049.json, 视频生成/图生视频/2052258401169752065.json, 视频生成/图生视频/2070131687614406658.json, 视频生成/图生视频/2075910446967779329.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2083148321954291714.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093644198363881473.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093676510929575938.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101617649074659330.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101629864922140674.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2105246871684993026.json, 视频生成/图生视频/2052185338583498754.json, 视频生成/图生视频/2057694453565054977.json, 视频生成/图生视频/2045576012469112833.json, 视频生成/图生视频/2056262316534091777.json, 视频生成/图生视频/2056538120484638722.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2096031121212530690.json, 视频生成/图生视频/2052610922312679426.json, 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2018039225307893762.json、视频生成/图生视频/1979808803409530882.json、视频生成/图生视频/2053339197372674049.json、视频生成/图生视频/2052258401169752065.json、视频生成/图生视频/2070131687614406658.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 19/20 个有
- `GIMMVFI_interpolate` —— 19/20 个有
- `PrimitiveInt` —— 19/20 个有
- `ImageConcatMulti` —— 18/20 个有
- `Int` —— 18/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/20 个有
- `PainterVRAM` —— 18/20 个有
- `Text Multiline` —— 2/20 个有
- `ImageFromBatch+` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `MathExpression|pysssss` —— 1/20 个有
- `ResizeLongestToNode` —— 1/20 个有
- `SaveImage` —— 1/20 个有
- `Text Concatenate` —— 1/20 个有
- `ttN seed` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 85% |
| Prompt 约束强度(CFG) | 12 | 6 - 20 | 20 | 82% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler | - | 20 | 95% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 85%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 20，20 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，20 个样本，一致性 95%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
