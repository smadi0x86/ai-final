# Copyright (c) 2021 Microsoft
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

variable "resource_group" {
}

variable "workspace_display_name" {
}

variable "location" {
}

variable "deploy_aks" {
}

variable "prefix" {
  type = string
}

variable "subscription_id" {

}

resource "random_string" "postfix" {
  length  = 6
  special = false
  upper   = false
}
