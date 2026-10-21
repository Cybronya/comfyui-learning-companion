---
name: unknown_workflow_video_upscale_latent_upscale_13
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.423684
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json, 视频生成/图生视频/h3图生视频gy_2087784031445413890.json, 视频生成/图生视频/minimax h3电商产品_2095444070079492097.json, 视频生成/图生视频/测试01剧本 YZ金鱼-MiniMax H3-多参考生视频-优化版_2107313229809672193.json, 视频生成/图生视频/进阶版！MiniMax H3 Ref2VA 多参生视频工作流_2102256455968710658.json, 视频生成/图生视频/金鱼-多参考生视频-电影感_2094788063007432706.json, 视频生成/文生视频/MiniMax H3-双采多参考生视频-优化版（解决画面油、一致性、生成慢问题） 用RH最基础的配置_2094800335167639554.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2096048331687555073.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2104154909896699906.json, 视频生成/文生视频/MiniMax H3-多参考生视频-最新优化版_2104888496719745025.json, 视频生成/文生视频/MiniMax H3-多参考生视频_2095195704401682433.json, 视频生成/文生视频/MiniMax H3-多图多音频视频参考生视频-无水印优化版_2095090395578462210.json, 视频生成/文生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2092878871120142337.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版（自用）_2094632571828260866.json, 视频生成/文生视频/【去油人脸一致】MiniMax H3全能多参考潜空间放大_2094826523541983233.json, 视频生成/文生视频/咩咩咩 MiniMax H3-多参考生视频双采_2096479303428038658.json, 视频生成/文生视频/多参考生视频-优化版_2095077768978591746.json, 视频生成/文生视频/工作流lin_2099078938155896833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_13

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json、视频生成/图生视频/h3图生视频gy_2087784031445413890.json、视频生成/图生视频/minimax h3电商产品_2095444070079492097.json、视频生成/图生视频/测试01剧本 YZ金鱼-MiniMax H3-多参考生视频-优化版_2107313229809672193.json、视频生成/图生视频/进阶版！MiniMax H3 Ref2VA 多参生视频工作流_2102256455968710658.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：42%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 18/19 个有
- `Text` —— 18/19 个有
- `easy float` —— 18/19 个有
- `忽略多组孤海` —— 17/19 个有
- `LoadAudio` —— 16/19 个有
- `VHS_LoadVideo` —— 16/19 个有
- `AudioCrop` —— 1/19 个有
- `CR Text` —— 1/19 个有
- `ComfySwitchNode` —— 1/19 个有
- `Compare` —— 1/19 个有
- `Fans Text Concatenate` —— 1/19 个有
- `GetImageSize` —— 1/19 个有
- `INTConstant` —— 1/19 个有
- `Int` —— 1/19 个有
- `Label (rgthree)` —— 1/19 个有
- `MiniMaxH3ImageToVideo` —— 1/19 个有
- `PreviewAudio` —— 1/19 个有
- `Seed Everywhere` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
