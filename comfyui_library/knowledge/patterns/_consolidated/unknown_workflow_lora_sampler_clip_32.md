---
name: unknown_workflow_lora_sampler_clip_32
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8653
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DapaoImageRatioLimitNode, EmptyLatentImage, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/001.Z-image生图巅峰024.随机美女抽卡or洗图_2042252208422526977.json, 图片生成/文生图/001.Z-image生图巅峰023.随机美女抽卡机_2041536436695994370.json, 图片生成/文生图/RPG角色卡 随机美女孵蛋器 V2升级版【角色卡模式】_2039603421052932097.json, 图片生成/文生图/ZT+ZB文生图参考自动优化20260406_2041136071802621954.json, 图片生成/文生图/ZT角色卡文生图20260407_2041458720655282177.json, 图片生成/文生图/Zimage随机美少女抽卡机【无限出图模式】_2059903175817252865.json, 图片生成/文生图/美女 孵蛋器 最新版【无限模式】_2041501084815990786.json, 图片生成/文生图/美女孵蛋器 V3升级版【无限模式】_2073460891844177921.json, 图片生成/文生图/🥳随机美女孵蛋器 V3升级版【无限模式】20260407_2041458441293668354.json, 图片生成/文生图/🥳随机美女孵蛋器 V3升级版【无限模式】_2040331510699528194.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/001.Z-image生图巅峰024.随机美女抽卡or洗图_2042252208422526977.json、图片生成/文生图/001.Z-image生图巅峰023.随机美女抽卡机_2041536436695994370.json、图片生成/文生图/RPG角色卡 随机美女孵蛋器 V2升级版【角色卡模式】_2039603421052932097.json、图片生成/文生图/ZT+ZB文生图参考自动优化20260406_2041136071802621954.json、图片生成/文生图/ZT角色卡文生图20260407_2041458720655282177.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DapaoImageRatioLimitNode`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 9/10 个有
- `llama_cpp_instruct_adv` —— 8/10 个有
- `llama_cpp_model_loader` —— 8/10 个有
- `llama_cpp_parameters` —— 8/10 个有
- `DapaoImageAspectRatioResizeNode` —— 7/10 个有
- `LoadImage` —— 7/10 个有
- `ImpactSwitch` —— 6/10 个有
- `Note Plus (mtb)` —— 6/10 个有
- `DapaoImageWatermarkNode` —— 5/10 个有
- `DapaoSafeSaveImage` —— 3/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有
- `CLIPLoader` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `ZML_SwitchOutput` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy isNone` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | 864 - 864 | 10 | 100% |
| 高度 | 1536 | 1536 - 1536 | 10 | 100% |
| 采样步数 | randomize | - | 10 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 864，观测区间 864 - 864，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，10 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
