---
name: text_to_image_video_lora_sampler_30
type: Text To Image
frequency: 20
level: strong
coverage: 0.87795
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/BF16音频驱动动态图形数字人生成处理工具_2101027167839809538.json, 视频生成/图生视频/H3单人口播特调音频驱动数字人真人感自动扩写_2100295692534247425.json, 视频生成/图生视频/H3音频驱动数字人BF16高质量真人感自动扩写_2100292889673818113.json, 视频生成/图生视频/H3音频驱动数字人真人感自动扩写处理工具_2100291312791674882.json, 视频生成/图生视频/MINIMAX H3风扇三段变装展示双采加速流工作流，图生视频换装新奇创意方案_2107968249039253505.json, 视频生成/图生视频/MINIMAX H3风扇三段变装展示｜双采加速流出片快_2107679101975875585.json, 视频生成/图生视频/MINIMAX-H3打斗全自动模版｜战斗特效图生视频专用_2089450758877040642.json, 视频生成/图生视频/MINIMAX-H3打斗视频全自动｜首帧多图参考战斗特效_2089425408629493762.json, 视频生成/图生视频/MiniMax H3多图参考打斗全自动视频生成处理工具_2101044324170551298.json, 视频生成/图生视频/MiniMax-H3打斗专用全自动｜图生视频战斗特效_2089700417658773506.json, 视频生成/图生视频/MiniMax-H3热血战斗Qwen3.8提示词增强｜单图全自动战斗特效图生视频_2090419222039060481.json, 视频生成/图生视频/单人口播特调MiniMax H3音频驱动数字人真人感处理工具_2102114889262256129.json, 视频生成/图生视频/单人口播特调｜Minimax H3音频驱动数字人b25-49｜真人感自动扩写_2101878791286116354.json, 视频生成/图生视频/打斗专用全自动｜MINIMAX-H3战斗特效图生视频一键直出_2089424199805915137.json, 视频生成/图生视频/打斗视频专用全自动模版｜MINIMAX-H3战斗特效图生视频_2091649091871789058.json, 视频生成/图生视频/打斗视频全自动模版｜MINIMAX-H3 战斗特效图生视频_2089268317403049986.json, 视频生成/图生视频/打斗视频全自动模版｜MINIMAX-H3战斗特效图生视频_2091811960156418049.json, 视频生成/图生视频/音频驱动动态图形数字人匹配模式视频生成处理工具_2101028734324269057.json, 视频生成/文生视频/H3多图参考打斗全自动工作流 文生视频图生视频_2100307233627262978.json, 视频生成/文生视频/MiniMax-H3全自动工作流｜文生图文生视频图生视频三合一_2089689168518664193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/BF16音频驱动动态图形数字人生成处理工具_2101027167839809538.json、视频生成/图生视频/H3单人口播特调音频驱动数字人真人感自动扩写_2100295692534247425.json、视频生成/图生视频/H3音频驱动数字人BF16高质量真人感自动扩写_2100292889673818113.json、视频生成/图生视频/H3音频驱动数字人真人感自动扩写处理工具_2100291312791674882.json、视频生成/图生视频/MINIMAX H3风扇三段变装展示双采加速流工作流，图生视频换装新奇创意方案_2107968249039253505.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
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
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 17/20 个有
- `RH_LLMAPI_Pro_Node` —— 17/20 个有
- `LoraLoaderBypassModelOnly` —— 13/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 13/20 个有
- `PT_H3ConcatAVLatent` —— 13/20 个有
- `PrimitiveStringMultiline` —— 13/20 个有
- `VAEEncode` —— 13/20 个有
- `Fast Groups Bypasser (rgthree)` —— 11/20 个有
- `PreviewAny` —— 11/20 个有
- `SaveImage` —— 9/20 个有
- `CR Prompt Text` —— 7/20 个有
- `ShellAgentPluginOutputText` —— 7/20 个有
- `TrimAudioDuration` —— 7/20 个有
- `easy showAnything` —— 7/20 个有
- `LayerUtility: PurgeVRAM V2` —— 2/20 个有
- `Qwen3ASRLoader` —— 2/20 个有
- `Qwen3ASRTranscribe` —— 2/20 个有
- `H3SigmaRefiner` —— 1/20 个有
- `MemoryCleaner` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy saveText` —— 1/20 个有
- `llama_cpp_instruct_adv` —— 1/20 个有
- `llama_cpp_model_loader` —— 1/20 个有
- `llama_cpp_parameters` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
