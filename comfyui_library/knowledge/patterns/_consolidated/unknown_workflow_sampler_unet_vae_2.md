---
name: unknown_workflow_sampler_unet_vae_2
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.829862
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json, 视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json, 视频生成/图生视频/H3多参图生视频_2084177913167040514.json, 视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json, 视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json, 视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json, 视频生成/图生视频/MINIMAX-H3 多参工作流包含加速流程和完美克隆音频最终版_2087190952204132354.json, 视频生成/图生视频/MINIMAX-H3 多图生成视频_2085523161088610305.json, 视频生成/图生视频/MINIMAX-H3-图片加音频参考生视频-有提示词模板-int8和fp8_2084515925415522306.json, 视频生成/图生视频/MINIMAX-H3_2084691718737317889.json, 视频生成/图生视频/MINIMAX-H3_多图参考生视频_2084844223446208514.json, 视频生成/图生视频/MiniMax H3 R2V comfyorg_2085736828308643841.json, 视频生成/图生视频/MiniMax H3 R2V-8步 comfyorg_2087532854384349186.json, 视频生成/图生视频/2053733634456207362.json, 视频生成/图生视频/MiniMax H3 参考生视频_2084543006513909761.json, 视频生成/图生视频/MiniMax H3 参考生视频_2085194930540077058.json, 视频生成/图生视频/MiniMax H3 双角色+背景+自定义音频输入 视频生成工作流_2084953803597635586.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化 真人短剧剧情演绎_2084620840548786177.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化_2083480380576976897.json, 视频生成/图生视频/MiniMax H3全能参考+首帧+参考音频_2093611760375910402.json, 视频生成/图生视频/MiniMax H3全能参考+首帧+参考音频（一次解决声音一致性和角色一致性）_2088866600530309121.json, 视频生成/图生视频/MiniMax H3全能参考工作流_2086738528175747074.json, 视频生成/图生视频/Minimax H3 多参视频生成_2089987673200091137.json, 视频生成/图生视频/Minimax3-参考生视频-8月8日版_2086541785450500098.json, 视频生成/图生视频/全能参考+首帧+音频｜MiniMax H3声音角色双一致_2108370045545041922.json, 视频生成/文生视频/MiniMax H3满血无损全家桶_文生、单图、多图生视频_2087520237779509249.json, 视频生成/文生视频/MiniMax H3满血无损加速1.0高清工作流_2086726672409251842.json, 视频生成/文生视频/MiniMax H3满血无损高清加速版_2087462526824046593.json, 视频生成/文生视频/MiniMaxH3地表最强阿里3步加速Lora 全能参考速度起飞_2099733663037607937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/H3_24G_3refs_声音参考_2106668851638390785.json、视频生成/图生视频/H3单采版-无LoRA-480P_2099175040867725314.json、视频生成/图生视频/H3多参图生视频_2084177913167040514.json、视频生成/图生视频/MINIMAX H3多图参考生视频-lc_2088551068568477698.json、视频生成/图生视频/MINIMAX H3官方多参工作流_2098996477975687170.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 28/29 个有
- `VAEDecode` —— 28/29 个有
- `ComfyMathExpression` —— 27/29 个有
- `CreateVideo` —— 27/29 个有
- `PrimitiveFloat` —— 27/29 个有
- `SaveVideo` —— 26/29 个有
- `PrimitiveStringMultiline` —— 24/29 个有
- `LoadAudio` —— 22/29 个有
- `PathchSageAttentionKJ` —— 14/29 个有
- `VHS_LoadVideo` —— 13/29 个有
- `EasyCache` —— 12/29 个有
- `VHS_VideoCombine` —— 12/29 个有
- `Fast Groups Bypasser (rgthree)` —— 11/29 个有
- `LoraLoaderModelOnly` —— 8/29 个有
- `ModelPatchTorchSettings` —— 7/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/29 个有
- `JjkText` —— 4/29 个有
- `UniBlockSwap` —— 3/29 个有
- `SpectrumApplyMiniMaxH3` —— 2/29 个有
- `CR Prompt Text` —— 1/29 个有
- `LTXVSeparateAVLatent` —— 1/29 个有
- `Label (rgthree)` —— 1/29 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/29 个有
- `PrimitiveInt` —— 1/29 个有
- `RTXVideoSuperResolution` —— 1/29 个有
- `VAEDecodeTiled` —— 1/29 个有
- `忽略多组孤海` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
