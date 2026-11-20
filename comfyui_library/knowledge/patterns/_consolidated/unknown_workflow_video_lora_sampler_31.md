---
name: unknown_workflow_video_lora_sampler_31
type: Unknown Workflow
frequency: 26
level: strong
coverage: 0.964538
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json, 数字人/数字人/Lemonkid  抖音短视频生成测试_2056611700207611905.json, 数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json, 视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json, 视频生成/图生视频/wan2.2电商服装展示_模特360°演示视频保持一致性_2053339197372674049.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2052258401169752065.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2070131687614406658.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2075910446967779329.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2083148321954291714.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093644198363881473.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093676510929575938.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101617649074659330.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101629864922140674.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2105246871684993026.json, 视频生成/图生视频/图生视频 -电商专用_模特演示视频-wan2.2_2052185338583498754.json, 视频生成/图生视频/电商服装展示 360度展示 人物动态展示 人物原地转身旋转 模特演示视频 wan2.2_2057694453565054977.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2045576012469112833.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2056262316534091777.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2056538120484638722.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2096031121212530690.json, 视频生成/图生视频/超好用🔥电商服装展示-模特产品展示视频-wan2.2_2052610922312679426.json, 视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json, 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json, 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json, 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json, 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json、数字人/数字人/Lemonkid  抖音短视频生成测试_2056611700207611905.json、数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json、视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json、视频生成/图生视频/wan2.2电商服装展示_模特360°演示视频保持一致性_2053339197372674049.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 25/26 个有
- `PrimitiveInt` —— 25/26 个有
- `SimpleMath+` —— 25/26 个有
- `LoadImage` —— 22/26 个有
- `WanImageToVideo` —— 22/26 个有
- `ImageConcatMulti` —— 20/26 个有
- `Int` —— 20/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/26 个有
- `PainterVRAM` —— 20/26 个有
- `LayerUtility: PurgeVRAM V2` —— 5/26 个有
- `Text Multiline` —— 5/26 个有
- `EmptyHunyuanLatentVideo` —— 4/26 个有
- `Text Concatenate` —— 2/26 个有
- `LayerUtility: PurgeVRAM` —— 1/26 个有
- `MathExpression|pysssss` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 26 | 85% |
| Prompt 约束强度(CFG) | 12 | 6 - 20 | 26 | 79% |
| 采样算法 | 1 | 1 - 1 | 26 | 100% |
| 调度器 | euler | - | 26 | 96% |
| 重绘幅度 | simple | - | 26 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，26 个样本，一致性 85%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 20，26 个样本
- 采样算法 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，26 个样本，一致性 96%
- 重绘幅度 最常用 simple，26 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
