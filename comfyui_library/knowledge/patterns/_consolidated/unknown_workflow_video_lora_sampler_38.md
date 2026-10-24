---
name: unknown_workflow_video_lora_sampler_38
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.963083
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, INTConstant, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json, 视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json, 视频生成/图生视频/wan2.2电商服装展示_模特360°演示视频保持一致性_2053339197372674049.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2052258401169752065.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2075910446967779329.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2083148321954291714.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093644198363881473.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093676510929575938.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101617649074659330.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101629864922140674.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2105246871684993026.json, 视频生成/图生视频/图生视频 -电商专用_模特演示视频-wan2.2_2052185338583498754.json, 视频生成/图生视频/电商服装展示 360度展示 人物动态展示 人物原地转身旋转 模特演示视频 wan2.2_2057694453565054977.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2045576012469112833.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2056262316534091777.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2056538120484638722.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2096031121212530690.json, 视频生成/图生视频/超好用🔥电商服装展示-模特产品展示视频-wan2.2_2052610922312679426.json, 视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json, 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json, 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json, 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json, 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json、视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json、视频生成/图生视频/wan2.2电商服装展示_模特360°演示视频保持一致性_2053339197372674049.json、视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2052258401169752065.json、视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `INTConstant`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 20/24 个有
- `WanImageToVideo` —— 20/24 个有
- `ImageConcatMulti` —— 19/24 个有
- `Int` —— 19/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 19/24 个有
- `PainterVRAM` —— 19/24 个有
- `LayerUtility: PurgeVRAM V2` —— 5/24 个有
- `Text Multiline` —— 5/24 个有
- `EmptyHunyuanLatentVideo` —— 4/24 个有
- `Text Concatenate` —— 2/24 个有
- `MathExpression|pysssss` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 24 | 88% |
| Prompt 约束强度(CFG) | 12 | 8 - 20 | 24 | 80% |
| 采样算法 | 1 | 1 - 1 | 24 | 100% |
| 调度器 | euler | - | 24 | 100% |
| 重绘幅度 | simple | - | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，24 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 12，观测区间 8 - 20，24 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，24 个样本，一致性 100%
- 重绘幅度 最常用 simple，24 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
