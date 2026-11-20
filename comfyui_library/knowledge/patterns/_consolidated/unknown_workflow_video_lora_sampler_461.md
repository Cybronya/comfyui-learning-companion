---
name: unknown_workflow_video_lora_sampler_461
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.944714
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2万相通义图生视频极速电影级版_1950206253990592514.json, 视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json, 视频生成/图生视频/wan2.2图生视频（3分钟）_1982023168992919554.json, 视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json, 视频生成/图生视频/小狗生成视频_2009159986848473089.json, 视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json, 视频生成/图生视频/🦖Wan2.2 极速高质量_1950004149220982785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_461

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/wan2.2万相通义图生视频极速电影级版_1950206253990592514.json、视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json、视频生成/图生视频/wan2.2图生视频（3分钟）_1982023168992919554.json、视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json、视频生成/图生视频/小狗生成视频_2009159986848473089.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `ACE_ImageGetSize` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `ResizeLongestToNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 7 | 62% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | euler | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，7 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
