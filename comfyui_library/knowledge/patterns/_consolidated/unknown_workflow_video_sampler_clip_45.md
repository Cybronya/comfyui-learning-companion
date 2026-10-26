---
name: unknown_workflow_video_sampler_clip_45
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.975083
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 SVI2 Pro 10秒长视频_2036317087181840385.json, 视频生成/图生视频/Wan2.2-native-control-Inp_1955921227057647617.json, 视频生成/图生视频/smooth图生视频工作流_2067249517136797697.json, 视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json, 视频生成/图生视频/wan2.2图生视频（3分钟）_1982023168992919554.json, 视频生成/图生视频/图生视频工作流_2066459393683705858.json, 视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json, 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json, 视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json, 视频生成/文生视频/图+文生视频 -WanImageToVideo_1986023978202529793.json, 视频生成/文生视频/图生视频  (支持AI自动生成剧本)_1983914577035493377.json, 视频生成/文生视频/图生视频 (支持AI自动手动生成短视频剧本)_1985873348330696706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 SVI2 Pro 10秒长视频_2036317087181840385.json、视频生成/图生视频/Wan2.2-native-control-Inp_1955921227057647617.json、视频生成/图生视频/smooth图生视频工作流_2067249517136797697.json、视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json、视频生成/图生视频/wan2.2图生视频（3分钟）_1982023168992919554.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `ImageResizeKJv2` —— 6/12 个有
- `JWInteger` —— 6/12 个有
- `CLIPVisionEncode` —— 5/12 个有
- `CLIPVisionLoader` —— 5/12 个有
- `MathExpression|pysssss` —— 5/12 个有
- `Seed (rgthree)` —— 5/12 个有
- `CR Prompt Text` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `Int` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `easy textSwitch` —— 2/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `ConstrainImage|pysssss` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `ImageBatchExtendWithOverlap` —— 1/12 个有
- `ImageFromBatch+` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `WanAdvancedI2V` —— 1/12 个有
- `WanFunInpaintToVideo` —— 1/12 个有
- `easy batchAnything` —— 1/12 个有
- `ttN concat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 75% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 12 | 55% |
| 采样算法 | 1 | 1 - 3.5 | 12 | 34% |
| 调度器 | euler | - | 12 | 58% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，12 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 34%
- 调度器 最常用 euler，12 个样本，一致性 58%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
