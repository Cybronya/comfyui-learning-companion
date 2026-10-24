---
name: text_to_image_lora_sampler_clip_212
type: Text To Image
frequency: 9
level: strong
coverage: 0.865
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json, 视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json, 视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json, 视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json, 视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json, 视频生成/图生视频/漫剧林辰角色动态演绎 图生视频一键生成流畅画面_2104279422512754690.json, 视频生成/图生视频/短剧漫剧参考图生视频工作流，图生视频短剧制作方案_2103604319982542850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_212

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json、视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json、视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json、视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json、视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `SaveImage` —— 5/9 个有
- `DF_String_Concatenate` —— 3/9 个有
- `DF_Text_Box` —— 3/9 个有
- `JWStringGetLine` —— 3/9 个有
- `JjkConcat` —— 3/9 个有
- `JjkShowText` —— 3/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/9 个有
- `ReplaceString` —— 3/9 个有
- `StringConstant` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有

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
