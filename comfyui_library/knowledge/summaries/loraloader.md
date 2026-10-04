---
name: LoraLoader
title: LoraLoader（LoRA 加载器）
category: nodes
tags: [lora, model,内置节点, sd15]
updated: 2026-10-04
---

# LoraLoader

> 依据 comfyui_library/workflows/sd1.5/lora.png（ComfyUI 官方 LoRA 教程）实测分析补全。

## 作用
把 LoRA（Low-Rank Adaptation，低秩适配）权重注入已加载的模型。LoRA 文件很小（几 MB~几百 MB），
却能让基础模型获得新风格 / 新角色 / 新概念，是"一个底模 + N 个风格包"玩法的基础。
节点同时改写两路输出：MODEL（影响画面生成）和 CLIP（影响文本编码对触发词的响应）。

## 所属插件
ComfyUI 内置（comfy-core），无 custom_nodes 依赖。

## 关键参数
| 参数 | 说明 |
|---|---|
| lora_name | LoRA 文件路径（models/loras/ 下），如 `SD1.5\blindbox_V1Mix.safetensors` |
| strength_model | 模型权重强度。0=无效果，1.0=完全生效。控制画面风格改变的幅度 |
| strength_clip | 文本编码器强度。控制 LoRA 对提示词触发词响应的放大程度 |
| model / clip | 上游输入，必须接 CheckpointLoader（或上一个 LoraLoader）的对应输出 |

## 使用要点
- 接线位置：CheckpointLoader 之后、CLIPTextEncode / KSampler 之前。
- 串联叠加：多个 LoraLoader 首尾相接即可叠加多个 LoRA（每个再调一次强度）。
- CLIP 与 MODEL 可只取其一，另一路直连原输出。
- 本例取值 model 0.75 / clip 1.0：风格稍收敛、触发词响应拉满，是盲盒风 LoRA 的常见配置。

## 常见坑
- strength 过高（>1.2）易过饱和、构图崩坏；从 0.5~1.0 起步试。
- LoRA 与底模代际必须匹配：SD1.5 LoRA 不能用于 SDXL/Flux。
- 只改 strength_model 不改 strength_clip 时，触发词可能"叫不应"。

## 关联卡片
- comfyui_library/knowledge/patterns/sd15-t2i-basic.md（宿主模式）
- comfyui_library/knowledge/patterns/sd15-t2i-lora.md（本节点构成的模式）
