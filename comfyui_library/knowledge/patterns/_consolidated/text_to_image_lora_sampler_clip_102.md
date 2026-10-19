---
name: text_to_image_lora_sampler_clip_102
type: Text To Image
frequency: 9
level: strong
coverage: 0.883111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json, 视频生成/图生视频/Minimax H3冻结时间360环绕｜首尾画面循环闭环｜HyperFlow 8步LoRA加持_2104830891699822594.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2086209989152174082.json, 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json, 视频生成/图生视频/MinimaxH3故事板九宫格分镜-4步加速多参考图人物场景特效_2087363609331589121.json, 视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json, 视频生成/图生视频/lightx2v不同版加速Lora测试｜Minimax H3图生视频对比_2096727729675788289.json, 视频生成/图生视频/参考图生视频生成｜MiniMaxH3高质量出片工作流_2095049456667414529.json, 视频生成/文生视频/MiniMax h3 4步lora2加速版｜文生图生视频直出_2092366496205987842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json、视频生成/图生视频/Minimax H3冻结时间360环绕｜首尾画面循环闭环｜HyperFlow 8步LoRA加持_2104830891699822594.json、视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2086209989152174082.json、视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json、视频生成/图生视频/MinimaxH3故事板九宫格分镜-4步加速多参考图人物场景特效_2087363609331589121.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/9 个有
- `PrimitiveFloat` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `MiniMaxH3ImageToVideo` —— 5/9 个有
- `ModelAttentionBackend` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `MiniMaxH3Easy` —— 2/9 个有
- `MiniMaxH3EasyLoader` —— 2/9 个有
- `MiniMaxH3EasyOutput` —— 2/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `RTXVideoSuperResolution` —— 2/9 个有
- `TextInput_` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
